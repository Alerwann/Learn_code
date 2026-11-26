from app.db.mysql import get_db
from app.protocol.balise_info import BaliseInfoRepository
from app.repositories.balise_info import SqlBaliseInfoRepository
from app.schemas.balise_info import BaliseInfoIn, BaliseInfoOut
from app.services.balise_info import BaliseInfoNotFoundError, BaliseInfoService
from fastapi import APIRouter, Depends, HTTPException, Query, status
from pymysql.connections import Connection

router = APIRouter(prefix="/balises", tags=["balise_info"])


def get_balise_service(db: Connection = Depends(get_db)) -> BaliseInfoService:  # noqa: B008
    repository: BaliseInfoRepository = SqlBaliseInfoRepository(db)
    return BaliseInfoService(repository)


@router.post("", response_model=BaliseInfoOut, status_code=status.HTTP_201_CREATED)
def create_balise(
    payload: BaliseInfoIn,
    service: BaliseInfoService = Depends(get_balise_service),  # noqa: B008
) -> BaliseInfoOut:
    try:
        return service.create_balise(payload)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc


@router.get("", response_model=list[BaliseInfoOut])
def list_balises(
    limit: int = Query(default=100, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
    service: BaliseInfoService = Depends(get_balise_service),  # noqa: B008
) -> list[BaliseInfoOut]:
    return service.list_balises(limit=limit, offset=offset)


@router.get("/{balise_id}", response_model=BaliseInfoOut)
def get_balise(
    balise_id: int,
    service: BaliseInfoService = Depends(get_balise_service),  # noqa: B008
) -> BaliseInfoOut:
    try:
        return service.get_balise(balise_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc
    except BaliseInfoNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.put("/{balise_id}", response_model=BaliseInfoOut)
def update_balise(
    balise_id: int,
    payload: BaliseInfoIn,
    service: BaliseInfoService = Depends(get_balise_service),  # noqa: B008
) -> BaliseInfoOut:
    try:
        return service.update_balise(balise_id, payload)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc
    except BaliseInfoNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.delete("/{balise_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_balise(
    balise_id: int,
    service: BaliseInfoService = Depends(get_balise_service),  # noqa: B008
) -> None:
    try:
        service.delete_balise(balise_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc
    except BaliseInfoNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
