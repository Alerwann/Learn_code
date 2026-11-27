from app.db.mysql import get_db
from app.protocols.def_protocol import DefRepository
from app.repositories.definition_repo import SqlDefinitionRepo
from app.schemas.definition_shema import DefinititionIn, DefinititionOut
from app.services.definition_service import DefNotFoundError, DefService
from fastapi import APIRouter, Depends, HTTPException, status
from pymysql.connections import Connection

router = APIRouter(prefix="/def", tags=["defintion"])


def get_def_service(db: Connection = Depends(get_db)) -> DefService:  # noqa: B008
    repository: DefRepository = SqlDefinitionRepo(db)
    return DefService(repository)


@router.get("", response_model=list[DefinititionOut])
def list_def(service: DefService = Depends(get_def_service)) -> list[DefinititionOut]:  # noqa: B008
    return service.getAllDef()


@router.get("/{def_category}", response_model=DefinititionOut)
def getDefByCategory(
    def_category: str,
    service: DefService = Depends(get_def_service),  # noqa: B008
) -> DefinititionOut:
    try:
        return service.getDefByCategory(def_category)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)
        ) from exc
    except DefNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.get("/{def_id}", response_model=DefinititionOut)
def getDefById(
    def_id: int,
    service: DefService = Depends(get_def_service),  # noqa: B008
) -> DefinititionOut:
    try:
        return service.getDefByCategory(def_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)
        ) from exc
    except DefNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.post("", response_model=DefinititionOut, status_code=status.HTTP_201_CREATED)
def create_def(
    payload: DefinititionIn,
    service: DefService = Depends(get_def_service),  # noqa: B008
) -> DefinititionOut:
    try:
        return service.create_def(payload)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)
        ) from exc


@router.put("/{def_id}", response_model=DefinititionOut)
def update_def(
    def_id: int,
    playload: DefinititionIn,
    service: DefService = Depends(get_def_service),  # noqa: B008
):
    try:
        return service.updateDef(playload)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)
        ) from exc
    except DefNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.delete("/{def_id}", response_model=status.HTTP_204_NO_CONTENT)
def deleteCategory(
    def_id: int,
    service: DefService = Depends(get_def_service),  # noqa: B008
) -> None:
    try:
        service.deleteCategory(def_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)
        ) from exc
    except DefNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
