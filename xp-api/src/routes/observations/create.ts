import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { subscriptionGuard } from "../../utils/guards/subscription.guard.js";
import { z } from "zod";
import { tgGeoSchema } from "../../models/tg-geo.js";
import { tgMediaGroupItemSchema } from "../../models/tg-media-group-item.js";

const createObservationSchema = z.object({
  tgText: z.string().optional(),
  tgPhotoId: z.string().optional(),
  tgVideoId: z.string().optional(),
  tgVoiceId: z.string().optional(),
  tgDocumentId: z.string().optional(),
  tgVideoNoteId: z.string().optional(),
  tgGeo: tgGeoSchema.optional(),
  tgMediaGroup: z.array(tgMediaGroupItemSchema).optional(),
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
        tgDocumentId,
        tgGeo,
        tgMediaGroup,
        tgPhotoId,
        tgText,
        tgVideoId,
        tgVideoNoteId,
        tgVoiceId,
      });

      return reply.send({ observation });
    }
  );
};

export default createObservation;
