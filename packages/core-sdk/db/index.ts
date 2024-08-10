export {
  Experiment,
  Observation,
  ObservationView,
  Subscription,
  TgGeo,
  TgMediaGroupItem,
  User,
} from "@prisma/client";

import { PrismaClient } from "@prisma/client";

export const db = new PrismaClient({ log: ["error", "query"] });
