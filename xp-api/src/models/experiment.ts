import { z } from "zod";
import { PrismaSelectEntity } from "../utils/db/select-entity.js";
import { selectUser, userSchema } from "./user.js";
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

export const selectExperiment: PrismaSelectEntity<Experiment> = {
  canceledAt: true,
  completeBy: true,
  completedAt: true,
  createdAt: true,
  id: true,
  tgDocumentId: true,
  tgGeo: true,
  tgMediaGroup: true,
  tgPhotoId: true,
  tgText: true,
  tgVideoId: true,
  tgVideoNoteId: true,
  tgVoiceId: true,
  user: { select: selectUser },
};
