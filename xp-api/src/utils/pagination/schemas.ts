import { z } from "zod";

export const requestPaginationSchema = z.object({
  limit: z.coerce.number().int().optional(),
  cursor: z.string().min(1).optional(),
});
