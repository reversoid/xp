import { z } from "zod";
import { PrismaSelectEntity } from "../utils/db/select-entity.js";

export const userSchema = z.object({
  id: z.string(),
  email: z.string(),
  username: z.string(),
  createdAt: z.date(),
});

export type User = z.infer<typeof userSchema>;

export const selectUser: PrismaSelectEntity<User> = {
  createdAt: true,
  email: true,
  id: true,
  username: true,
};
