import { TgMediaGroupItem } from "../models/tg-media-group-item";
import { PrismaSelectEntity } from "./utils/select-entity";

export const selectTgMediaGroupItem: PrismaSelectEntity<TgMediaGroupItem> = {
  tgAudioId: true,
  tgDocumentId: true,
  tgPhotoId: true,
  tgVideoId: true,
};
