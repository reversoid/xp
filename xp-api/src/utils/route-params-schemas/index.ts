import { z } from "zod";

export const inivteIdSchema = z.string().min(10).max(10);

export const projectIdSchema = z.string().min(10).max(10);

export const loopIdSchema = z.coerce.number().int();
