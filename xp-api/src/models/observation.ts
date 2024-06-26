import { z } from "zod";
import { PrismaSelectEntity } from "../utils/db/select-entity.js";
import { selectUser, userSchema } from "./user.js";

const mediaGroupSchema = z.object({
  tgAudioId: z.string().nullable(),
  tgDocumentId: z.string().nullable(),
  tgPhotoId: z.string().nullable(),
  tgVideoId: z.string().nullable(),
});

export const observationSchema = z.object({
  id: z.string(),
  tgText: z.string().nullable(),
  tgPhotoId: z.string().nullable(),
  tgVideoId: z.string().nullable(),
  tgVoiceId: z.string().nullable(),
  tgDocumentId: z.string().nullable(),
  tgVideoNoteId: z.string().nullable(),
  tgMediaGroup: z.array(mediaGroupSchema),
  user: userSchema,
});

export type Observation = z.infer<typeof observationSchema>;

export const selectObservation: PrismaSelectEntity<Observation> = {
  id: true,
  tgText: true,
  tgDocumentId: true,
  tgMediaGroup: true,
  tgPhotoId: true,
  tgVideoId: true,
  tgVideoNoteId: true,
  tgVoiceId: true,
  user: { select: selectUser },
};
