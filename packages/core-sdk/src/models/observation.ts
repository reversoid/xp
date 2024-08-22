import { z } from "zod";
import { userSchema } from "./user.js";
import { tgGeoSchema } from "./tg-geo.js";
import { tgMediaGroupItemSchema } from "./tg-media-group-item.js";

export const observationSchema = z.object({
  id: z.string(),
  tgText: z.string().nullable(),
  tgPhotoId: z.string().nullable(),
  tgVideoId: z.string().nullable(),
  tgVoiceId: z.string().nullable(),
  tgDocumentId: z.string().nullable(),
  tgVideoNoteId: z.string().nullable(),
  tgGeo: tgGeoSchema.nullable(),
  tgMediaGroup: z.array(tgMediaGroupItemSchema),
  user: userSchema,
});

export type Observation = z.infer<typeof observationSchema>;
