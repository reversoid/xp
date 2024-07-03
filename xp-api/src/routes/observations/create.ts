import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { subscriptionGuard } from "../../utils/guards/subscription.guard.js";
import { z } from "zod";
import { tgGeoSchema } from "../../models/tg-geo.js";
import { tgMediaGroupItemSchema } from "../../models/tg-media-group-item.js";

const createObservationSchema = z.object({
  tgText: z.string().nullish(),
  tgPhotoId: z.string().nullish(),
  tgVideoId: z.string().nullish(),
  tgVoiceId: z.string().nullish(),
  tgDocumentId: z.string().nullish(),
  tgVideoNoteId: z.string().nullish(),
  tgGeo: tgGeoSchema.nullish(),
  tgMediaGroup: z.array(tgMediaGroupItemSchema).nullish(),
});

const createObservation: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const observationService = fastify.diContainer.resolve("observationService");

  fastify.post(
    "/",
    {
      preHandler: [authGuard, subscriptionGuard],
      schema: { body: createObservationSchema },
    },
    async function (request, reply) {
      const user = request.user!;

      const {
        tgDocumentId,
        tgGeo,
        tgMediaGroup,
        tgPhotoId,
        tgText,
        tgVideoId,
        tgVideoNoteId,
        tgVoiceId,
      } = request.body;

      const observation = await observationService.createObservation(user.id, {
        tgDocumentId: tgDocumentId ?? undefined,
        tgGeo: tgGeo ?? undefined,
        tgMediaGroup: tgMediaGroup ?? undefined,
        tgPhotoId: tgPhotoId ?? undefined,
        tgText: tgText ?? undefined,
        tgVideoId: tgVideoId ?? undefined,
        tgVideoNoteId: tgVideoNoteId ?? undefined,
        tgVoiceId: tgVoiceId ?? undefined,
      });

      return reply.send({ observation });
    }
  );
};

export default createObservation;
