import { z } from "zod";

export const tgMediaGroupItemSchema = z.object({
  tgAudioId: z.string().nullable(),
  tgDocumentId: z.string().nullable(),
  tgPhotoId: z.string().nullable(),
  tgVideoId: z.string().nullable(),
});

export type TgMediaGroupItem = z.infer<typeof tgMediaGroupItemSchema>;
