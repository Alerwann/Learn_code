export interface BaliseInfoOut {
  balise_id: number;
  balise_type: string;
  balise_nom: string;
  balise_exemple: string;
  balise_explication: string;
}

export interface BaliseInfoIn {
  balise_type: string;
  balise_nom: string;
  balise_exemple: string;
  balise_explication: string;
}
