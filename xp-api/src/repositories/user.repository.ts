import { PrismaClient } from "@prisma/client";
import { selectUser, User } from "../models/user.js";

export class UserRepository {
  private readonly prismaClient: PrismaClient;

  constructor({ prismaClient }: { prismaClient: PrismaClient }) {
    this.prismaClient = prismaClient;
  }

  async getUserByTgId(tgId: bigint): Promise<User | null> {
    return this.prismaClient.user.findUnique({
      where: { tgId },
      select: selectUser,
    });
  }
}
