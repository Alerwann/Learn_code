import { DifficulteEnum } from '../../../shared/models/difficulte_model.model';
import { ThemeEnum } from '../../../shared/models/theme_model.model';

export interface AccueilCard {
  id: string;
  title: string;
  description: string;
  theme: ThemeEnum;
  niveau: DifficulteEnum;
}
