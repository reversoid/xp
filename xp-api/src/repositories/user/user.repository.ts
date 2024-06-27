import { PrismaClient } from "@prisma/client";
import { selectUser, User } from "../../models/user.js";
import { CreateUserDto } from "./types.js";
import { IdGenerator } from "../../utils/db/create-id.js";

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

  async getUserPayment(userId: User["id"]) {
    const paidUser = await this.prismaClient.paidUser.findFirst({
      where: { userId },
      select: { createdAt: true, lastPaidAt: true },
    });

    if (!paidUser) {
      return null;
    }

    return { firstPaidAt: paidUser.createdAt, lastPaidAt: paidUser.lastPaidAt };
  }
}
