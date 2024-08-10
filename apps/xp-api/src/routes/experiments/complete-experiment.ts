import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { authGuard } from "../../utils/guards/auth.guard.js";
import { subscriptionGuard } from "../../utils/guards/subscription.guard.js";
import { z } from "zod";
import { tgGeoSchema } from "core-sdk/models/tg-geo.js";
import { tgMediaGroupItemSchema } from "core-sdk/models/tg-media-group-item.js";
import { NoActiveExperimentException } from "core-sdk/services";

const completeExperimentSchema = z.object({
  tgText: z.string(),
  tgPhotoId: z.string().nullish(),
  tgVideoId: z.string().nullish(),
  tgVoiceId: z.string().nullish(),
  tgDocumentId: z.string().nullish(),
  tgVideoNoteId: z.string().nullish(),
  tgGeo: tgGeoSchema.nullish(),
  tgMediaGroup: z.array(tgMediaGroupItemSchema).nullish(),
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
          tgDocumentId: tgDocumentId ?? undefined,
          tgGeo: tgGeo ?? undefined,
          tgMediaGroup: tgMediaGroup ?? undefined,
          tgPhotoId: tgPhotoId ?? undefined,
          tgVideoId: tgVideoId ?? undefined,
          tgVideoNoteId: tgVideoNoteId ?? undefined,
          tgVoiceId: tgVoiceId ?? undefined,
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
