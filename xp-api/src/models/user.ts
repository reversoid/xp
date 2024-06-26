import { z } from "zod";
import { PrismaSelectEntity } from "../utils/db/select-entity.js";

export const userSchema = z.object({
  id: z.string(),
  tgId: z.bigint(),
  tgUsername: z.string(),
  createdAt: z.date(),
});

export type User = z.infer<typeof userSchema>;

export const selectUser: PrismaSelectEntity<User> = {
  id: true,
  tgId: true,
  tgUsername: true,
  createdAt: true,
};
