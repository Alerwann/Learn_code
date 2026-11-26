export interface BaliseInfoOut {
  balise_id: number;
  balise_type: string;
  balise_nom: string;
  balise_exemple: string;
  balise_description: string;
}

export interface BaliseInfoIn {
  balise_type: string;
  balise_nom: string;
  balise_exemple: string;
  balise_description: string;
}
