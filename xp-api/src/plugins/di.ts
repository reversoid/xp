import fp from "fastify-plugin";
import { fastifyAwilixPlugin } from "@fastify/awilix";
import { diContainer } from "@fastify/awilix";
import { Lifetime, asClass, asValue } from "awilix";
import { LoopRepository } from "../repositories/loop/loop.repository.js";
import { LoopService } from "../services/loop/loop.service.js";
import { ProjectRepository } from "../repositories/project/project.repository.js";
import { ProjectService } from "../services/project/project.service.js";
import { UserRepository } from "../repositories/user/user.repository.js";
import { UserService } from "../services/user/user.service.js";
import { AuthService } from "../services/auth/auth.service.js";
import fastifyRedis from "@fastify/redis";
import { PrismaClient } from "@prisma/client";
import { Lucia } from "lucia";
import { InviteRepository } from "../repositories/invite/invite.repository.js";
import { InviteService } from "../services/invite/invite.service.js";

declare module "@fastify/awilix" {
  interface Cradle {
    loopRepository: LoopRepository;
    loopService: LoopService;

    userRepository: UserRepository;
    userService: UserService;

    projectRepository: ProjectRepository;
    projectService: ProjectService;

    inviteService: InviteService;
    inviteRepository: InviteRepository;

    authService: AuthService;

    redisClient: fastifyRedis.FastifyRedis;
    prismaClient: PrismaClient;

    lucia: Lucia<Record<never, never>, Record<never, never>>;
  }
}

const initDI = ({
  redisClient,
  prismaClient,
  lucia,
}: {
  redisClient: fastifyRedis.FastifyRedis;
  prismaClient: PrismaClient;
  lucia: Lucia;
}) => {
  diContainer.register({
    userRepository: asClass(UserRepository, {
      lifetime: Lifetime.SINGLETON,
    }),
    userService: asClass(UserService, {
      lifetime: Lifetime.SINGLETON,
    }),

    loopRepository: asClass(LoopRepository, {
      lifetime: Lifetime.SINGLETON,
    }),
    loopService: asClass(LoopService, {
      lifetime: Lifetime.SINGLETON,
    }),

    projectRepository: asClass(ProjectRepository, {
      lifetime: Lifetime.SINGLETON,
    }),
    projectService: asClass(ProjectService, {
      lifetime: Lifetime.SINGLETON,
    }),

    authService: asClass(AuthService, {
      lifetime: Lifetime.SINGLETON,
    }),

    inviteRepository: asClass(InviteRepository, {
      lifetime: Lifetime.SINGLETON,
    }),

    inviteService: asClass(InviteService, {
      lifetime: Lifetime.SINGLETON,
    }),

    redisClient: asValue(redisClient),
    prismaClient: asValue(prismaClient),

    lucia: asValue(lucia),
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
      redisClient: fastify.redis,
      prismaClient: fastify.prisma,
      lucia: fastify.lucia,
    });
  },
  { dependencies: ["redis", "prisma", "lucia"] }
);
