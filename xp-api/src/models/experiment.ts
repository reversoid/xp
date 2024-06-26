import { z } from "zod";
import { PrismaSelectEntity } from "../utils/db/select-entity.js";
import { selectUser, userSchema } from "./user.js";

const mediaGroupSchema = z.object({
  tgAudioId: z.string().nullable(),
  tgDocumentId: z.string().nullable(),
  tgPhotoId: z.string().nullable(),
  tgVideoId: z.string().nullable(),
});

const geoSchema = z.object({
  longitude: z.number(),
  latitude: z.number(),
  horizontalAccuracy: z.number().nullable(),
});

export const experimentSchema = z.object({
  id: z.string(),
  user: userSchema,
  tgText: z.string().nullable(),
  tgPhotoId: z.string().nullable(),
  tgVideoId: z.string().nullable(),
  tgVoiceId: z.string().nullable(),
  tgDocumentId: z.string().nullable(),
  tgVideoNoteId: z.string().nullable(),
  tgGeo: geoSchema.nullable(),
  tgMediaGroup: z.array(mediaGroupSchema),
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
