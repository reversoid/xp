import { preHandlerHookHandler } from "fastify";

export const paymentGuard: preHandlerHookHandler = (
  request,
  response,
  done
) => {
  if (!request.paymentInfo || new Date() > request.paymentInfo.paidUntil) {
    done({
      code: "403",
      message: "NOT_PAID",
      name: "PAYMENT",
      statusCode: 403,
    });
  }

  done();
};
