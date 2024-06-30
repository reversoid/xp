import { preHandlerHookHandler } from "fastify";

export const authGuard: preHandlerHookHandler = (request, response, done) => {
  if (!request.user) {
    done({
      code: "401",
      message: "UNAUTHORIZED",
      name: "AUTH",
      statusCode: 401,
    });
  }

  done();
};
