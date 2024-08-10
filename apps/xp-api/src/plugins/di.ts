import fp from "fastify-plugin";
import { fastifyAwilixPlugin } from "@fastify/awilix";
import { diContainer } from "@fastify/awilix";
import { asClass, Lifetime } from "awilix";
import { PrismaClient } from "@prisma/client";

import {
  UserService,
  AuthService,
  ExperimentService,
  ObservationService,
  SubscriptionService,
} from "core-sdk/services";

declare module "@fastify/awilix" {
  interface Cradle {
    prismaClient: PrismaClient;

    userService: UserService;

    observationService: ObservationService;

    experimentService: ExperimentService;

    subscriptionService: SubscriptionService;

    authService: AuthService;
  }
}

const initDI = () => {
  diContainer.register({
    userService: asClass(UserService, {
      lifetime: Lifetime.SINGLETON,
    }),

    observationService: asClass(ObservationService, {
      lifetime: Lifetime.SINGLETON,
    }),

    experimentService: asClass(ExperimentService, {
      lifetime: Lifetime.SINGLETON,
    }),

    subscriptionService: asClass(SubscriptionService, {
      lifetime: Lifetime.SINGLETON,
    }),

    authService: asClass(AuthService, { lifetime: Lifetime.SINGLETON }),
  });
};

export default fp(
  async (fastify) => {
    fastify.register(fastifyAwilixPlugin, {
      disposeOnClose: true,
      disposeOnResponse: true,
      strictBooleanEnforced: true,
    });

    initDI();
  },
  { name: "di" }
);
