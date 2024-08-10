import { z } from "zod";

export const subscriptionSchema = z.object({
  createdAt: z.date(),
  until: z.date(),
});

export type Subscription = z.infer<typeof subscriptionSchema>;
