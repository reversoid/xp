import { z } from "zod";
import { userSchema } from "./user.js";
import { tgGeoSchema } from "./tg-geo.js";
import { tgMediaGroupItemSchema } from "./tg-media-group-item.js";

export const experimentSchema = z.object({
  id: z.string(),
  user: userSchema,
  tgText: z.string().nullable(),
  tgPhotoId: z.string().nullable(),
  tgVideoId: z.string().nullable(),
  tgVoiceId: z.string().nullable(),
  tgDocumentId: z.string().nullable(),
  tgVideoNoteId: z.string().nullable(),
  tgGeo: tgGeoSchema.nullable(),
  tgMediaGroup: z.array(tgMediaGroupItemSchema),
  createdAt: z.date(),
  completeBy: z.date(),
  completedAt: z.date().nullable(),
  canceledAt: z.date().nullable(),
});

export type Experiment = z.infer<typeof experimentSchema>;
