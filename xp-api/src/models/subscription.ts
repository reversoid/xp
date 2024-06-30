import { z } from "zod";
import { PrismaSelectEntity } from "../utils/db/select-entity.js";

export const subscriptionSchema = z.object({
  createdAt: z.date(),
  until: z.date(),
});

export type Subscription = z.infer<typeof subscriptionSchema>;

export const selectSubscription: PrismaSelectEntity<Subscription> = {
  createdAt: true,
  until: true,
};
