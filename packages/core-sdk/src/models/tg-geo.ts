import { z } from "zod";

export const tgGeoSchema = z.object({
  longitude: z.number(),
  latitude: z.number(),
  horizontalAccuracy: z.number().nullable(),
});

export type TgGeo = z.infer<typeof tgGeoSchema>;
