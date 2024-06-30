import { z } from "zod";
import { PrismaSelectEntity } from "../utils/db/select-entity.js";

export const tgGeoSchema = z.object({
  longitude: z.number(),
  latitude: z.number(),
  horizontalAccuracy: z.number().nullable(),
});

export type TgGeo = z.infer<typeof tgGeoSchema>;

export const selectTgGeo: PrismaSelectEntity<TgGeo> = {
  horizontalAccuracy: true,
  latitude: true,
  longitude: true,
};
