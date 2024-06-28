import { TgGeo } from "../../models/tg-geo.js";
import { TgMediaGroupItem } from "../../models/tg-media-group-item.js";

export type UpdateExperimentDto = {
  tgText: string;
  tgPhotoId?: string;
  tgVideoId?: string;
  tgVoiceId?: string;
  tgDocumentId?: string;
  tgVideoNoteId?: string;
  tgGeo?: TgGeo;
  tgMediaGroup?: Partial<TgMediaGroupItem>[];
};
