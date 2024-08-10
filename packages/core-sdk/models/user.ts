import { z } from "zod";

export const userSchema = z.object({
  id: z.string(),
  tgId: z.bigint(),
  tgUsername: z.string(),
  createdAt: z.date(),
});

export type User = z.infer<typeof userSchema>;
