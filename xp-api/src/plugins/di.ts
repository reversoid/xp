import fp from "fastify-plugin";
import { fastifyAwilixPlugin } from "@fastify/awilix";
import { diContainer } from "@fastify/awilix";
import { asClass, asValue, Lifetime } from "awilix";
import { PrismaClient } from "@prisma/client";
import { UserRepository } from "../repositories/user/user.repository.js";
import { UserService } from "../services/user/user.service.js";
import { ObservationRepository } from "../repositories/observation/observation.repository.js";
import { ObservationService } from "../services/observation/observation.service.js";

declare module "@fastify/awilix" {
  interface Cradle {
    prismaClient: PrismaClient;

    userRepository: UserRepository;
    userService: UserService;

    observationRepository: ObservationRepository;
    observationService: ObservationService;
  }
}

const initDI = ({ prismaClient }: { prismaClient: PrismaClient }) => {
  diContainer.register({
    userRepository: asClass(UserRepository, {
      lifetime: Lifetime.SINGLETON,
    }),
    userService: asClass(UserService, {
      lifetime: Lifetime.SINGLETON,
    }),

    observationRepository: asClass(ObservationRepository, {
      lifetime: Lifetime.SINGLETON,
    }),
    observationService: asClass(ObservationService, {
      lifetime: Lifetime.SINGLETON,
    }),

    prismaClient: asValue(prismaClient),
  });
};

export default fp(
  async (fastify) => {
    fastify.register(fastifyAwilixPlugin, {
      disposeOnClose: true,
      disposeOnResponse: true,
      strictBooleanEnforced: true,
    });

    initDI({
      prismaClient: fastify.prisma,
    });
  },
  { name: "di", dependencies: ["prisma"] }
);
