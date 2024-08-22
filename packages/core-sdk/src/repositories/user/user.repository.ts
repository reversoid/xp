import { PrismaClient } from "@prisma/client";
import { User } from "../../models/user.js";
import { CreateUserDto } from "./types.js";
import { IdGenerator } from "../utils/id-generator.js";
import { PrismaSelectEntity } from "../utils/select-entity.js";

export const selectUser: PrismaSelectEntity<User> = {
  id: true,
  createdAt: true,
  tgId: true,
  tgUsername: true,
};

export class UserRepository {
  private readonly prismaClient: PrismaClient;

  private readonly idGenerator = new IdGenerator("user");

  constructor({ prismaClient }: { prismaClient: PrismaClient }) {
    this.prismaClient = prismaClient;
  }

  async createUser(dto: CreateUserDto): Promise<User> {
    return this.prismaClient.user.create({
      data: {
        id: this.idGenerator.generateId(),
        tgId: dto.tgId,
        tgUsername: dto.tgUsername,
      },
      select: selectUser,
    });
  }

  async getUserByTgId(tgId: bigint): Promise<User | null> {
    return this.prismaClient.user.findUnique({
      where: { tgId },
      select: selectUser,
    });
  }
}
