import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { z } from "zod";

const deleteObservation: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const observationService = fastify.diContainer.resolve("observationService");

  fastify.patch(
    "/:observationId",
    {
      // TODO need admin auth handler?
      preHandler: [],
      schema: {
        params: z.object({ observationId: z.string().min(10).max(10) }),
      },
    },
    async function (request, reply) {
      const observationId = request.params.observationId;
      const observation = await observationService.approveObservation(
        observationId
      );

      return reply.send({ observation });
    }
  );
};

export default deleteObservation;