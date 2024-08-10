import { PrismaSelectEntity } from "./utils/select-entity";
import { TgGeo } from "../models/tg-geo";

export const selectTgGeo: PrismaSelectEntity<TgGeo> = {
  horizontalAccuracy: true,
  latitude: true,
  longitude: true,
};
