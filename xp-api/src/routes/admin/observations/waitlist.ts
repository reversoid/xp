import { FastifyPluginAsyncZod } from "fastify-type-provider-zod";
import { z } from "zod";

const deleteObservation: FastifyPluginAsyncZod = async (
  fastify
): Promise<void> => {
  const observationService = fastify.diContainer.resolve("observationService");

  // fastify.addHook("preHandler", (reqest, reply) => {
  //   // TODO check for admin
  //   return;
  // });

  fastify.get("/waitlist/amount", async function (request, reply) {
    const amount = await observationService.getWaitingObservationsAmount();

    return reply.send({ amount });
  });

  fastify.get(
    "/waitlist",
    {
      schema: {
        querystring: z.object({
          limit: z.coerce.number(),
          cursor: z.string().optional(),
        }),
      },
    },
    async function (request, reply) {
      const limit = request.query.limit;
      const cursor = request.query.cursor;

      const observations = await observationService.getWaitingObservations(
        limit,
        cursor
      );

      return reply.send({ observations });
    }
  );

  fastify.patch(
    "/waitlist/:observationId",
    {
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

  fastify.delete(
    "/waitlist/:observationId",
    {
      schema: {
        params: z.object({ observationId: z.string().min(10).max(10) }),
      },
    },
    async function (request, reply) {
      const observationId = request.params.observationId;
      await observationService.deleteObservation(observationId);

      return reply.send();
    }
  );
};

export default deleteObservation;
