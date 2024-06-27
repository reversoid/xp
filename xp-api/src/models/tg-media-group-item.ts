import { z } from "zod";
import { PrismaSelectEntity } from "../utils/db/select-entity.js";

export const tgMediaGroupItemSchema = z.object({
  tgAudioId: z.string().nullable(),
  tgDocumentId: z.string().nullable(),
  tgPhotoId: z.string().nullable(),
  tgVideoId: z.string().nullable(),
});

export type TgMediaGroupItem = z.infer<typeof tgMediaGroupItemSchema>;

export const selectTgMediaGroupItem: PrismaSelectEntity<TgMediaGroupItem> = {
  tgAudioId: true,
  tgDocumentId: true,
  tgPhotoId: true,
  tgVideoId: true,
};
