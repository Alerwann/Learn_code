export interface BaliseInfoOut {
  balise_id: number;
  balise_type: string;
  balise_name: string;
  balise_exemple: string;
  balise_explication: string;
}

export interface BaliseInfoIn {
  balise_type: string;
  balise_name: string;
  balise_exemple: string;
  balise_explication: string;
}
