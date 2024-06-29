import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { subscriptionGuard } from "../../utils/guards/subscription.guard.js";
import { NoActiveExperimentException } from "../../services/experiment/errors.js";
import { z } from "zod";
import { tgGeoSchema } from "../../models/tg-geo.js";
import { tgMediaGroupItemSchema } from "../../models/tg-media-group-item.js";

const completeExperimentSchema = z.object({
  tgText: z.string(),
  tgPhotoId: z.string().optional(),
  tgVideoId: z.string().optional(),
  tgVoiceId: z.string().optional(),
  tgDocumentId: z.string().optional(),
  tgVideoNoteId: z.string().optional(),
  tgGeo: tgGeoSchema.optional(),
  tgMediaGroup: z.array(tgMediaGroupItemSchema).optional(),
});

const completeExperiment: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const experimentService = fastify.diContainer.resolve("experimentService");

  fastify.patch(
    "/",
    {
      preHandler: [authGuard, subscriptionGuard],
      schema: { body: completeExperimentSchema },
    },
    async function (request, reply) {
      const user = request.user!;
      const {
        tgText,
        tgDocumentId,
        tgGeo,
        tgMediaGroup,
        tgPhotoId,
        tgVideoId,
        tgVideoNoteId,
        tgVoiceId,
      } = request.body;

      try {
        const experiment = await experimentService.completeExperiment(user.id, {
          tgText,
          tgDocumentId,
          tgGeo,
          tgMediaGroup,
          tgPhotoId,
          tgVideoId,
          tgVideoNoteId,
          tgVoiceId,
        });

        return reply.send({ experiment });
      } catch (error) {
        if (error instanceof NoActiveExperimentException) {
          return reply.conflict("NO_ACTIVE_EXPERIMENT");
        }

        throw error;
      }
    }
  );
};

export default completeExperiment;
