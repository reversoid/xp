import { TgGeo } from "../../models/tg-geo.js";
import { TgMediaGroupItem } from "../../models/tg-media-group-item.js";

export type CreateObservationDto = {
  tgText?: string;
  tgPhotoId?: string;
  tgVideoId?: string;
  tgVoiceId?: string;
  tgDocumentId?: string;
  tgVideoNoteId?: string;

  tgMediaGroup?: Array<Partial<TgMediaGroupItem>>;
  tgGeo?: TgGeo;
};
