import { preHandlerHookHandler } from "fastify";

export const paymentGuard: preHandlerHookHandler = (
  request,
  response,
  done
) => {
  // TODO check for payment info dates
  if (!request.paymentInfo) {
    done({
      code: "403",
      message: "NOT_PAID",
      name: "PAYMENT",
      statusCode: 403,
    });
  }

  done();
};
