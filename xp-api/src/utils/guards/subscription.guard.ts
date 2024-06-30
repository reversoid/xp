import { preHandlerHookHandler } from "fastify";

export const subscriptionGuard: preHandlerHookHandler = (
  request,
  response,
  done
) => {
  if (!request.subscription || request.subscription.until < new Date()) {
    done({
      code: "403",
      message: "NOT_PAID",
      name: "PAYMENT",
      statusCode: 403,
    });
  }

  done();
};
