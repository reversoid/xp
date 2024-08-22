import { PrismaClient } from "@prisma/client";
import { User } from "../../models/user.js";
import { CreateObservationDto } from "./types.js";
import { IdGenerator } from "../../utils/db/create-id.js";
import {
  Observation,
  observationSchema,
  selectObservation,
} from "../../models/observation.js";
import { TgGeo } from "../../models/tg-geo.js";
import {
  selectTgMediaGroupItem,
  TgMediaGroupItem,
} from "../../models/tg-media-group-item.js";
import { decodeCursor, encodeCursor } from "../../utils/pagination/cursor.js";
import { PaginatedData } from "../../utils/pagination/paginated-data.js";

export class ObservationRepository {
  private readonly prismaClient: PrismaClient;

  private readonly idGenerator = new IdGenerator("observation");

  constructor({ prismaClient }: { prismaClient: PrismaClient }) {
    this.prismaClient = prismaClient;
  }

  async markObservationAsSeen(
    userId: User["id"],
    observationId: Observation["id"]
  ) {
    await this.prismaClient.observationView.upsert({
      create: { userId, observationId },
      update: { createdAt: new Date() },
      where: { observationId_userId: { observationId, userId } },
    });
  }

  async getUserObservations(
    userId: User["id"],
    options: { limit: number; creationOrder: "asc" | "desc"; cursor?: string }
  ): Promise<PaginatedData<Observation>> {
    const decodedCursor = options.cursor ? decodeCursor(options.cursor) : null;

    const observations = await this.prismaClient.observation.findMany({
      where: { userId },
      take: options.limit + 1,
      orderBy: {
        privateId: options.creationOrder,
      },
      select: { ...selectObservation, privateId: true },

      cursor: decodedCursor ? { privateId: decodedCursor } : undefined,
    });

    const cursor = observations.at(options.limit)?.privateId;

    return {
      items: observations
        .slice(0, options.limit)
        .map((o) => observationSchema.parse(o)),
      cursor: cursor ? encodeCursor(cursor) : null,
    };
  }

  async getRandomUnseenObservations(
    userId: User["id"],
    limit: number
  ): Promise<Observation[]> {
    const ids = (await this.prismaClient.$queryRaw`
      SELECT o.id
      FROM observations o
      LEFT JOIN observation_views ov
      ON o.id = ov.observation_id
      AND ov.user_id = ${userId}
      WHERE ov.user_id IS NULL
      AND o.user_id != ${userId}
      AND o.is_approved = true
      ORDER BY RANDOM()
      LIMIT ${limit};
    `) as { id: Observation["id"] }[];

    return this.prismaClient.observation.findMany({
      where: { id: { in: ids.map((i) => i.id) } },
      select: selectObservation,
    });
  }

  async createObservation(
    userId: User["id"],
    dto: CreateObservationDto
  ): Promise<Observation> {
    return this.prismaClient.$transaction(async (tx) => {
      const observation = await tx.observation.create({
        data: {
          userId,
          id: this.idGenerator.generateId(),
          tgDocumentId: dto.tgDocumentId,
          tgText: dto.tgText,
          tgPhotoId: dto.tgPhotoId,
          tgVideoId: dto.tgVideoId,
          tgVideoNoteId: dto.tgVideoNoteId,
          tgVoiceId: dto.tgVoiceId,
        },
        select: selectObservation,
      });

      let tgGeo: TgGeo | null = null;
      if (dto.tgGeo) {
        tgGeo = await tx.tgGeo.create({
          data: {
            latitude: dto.tgGeo.latitude,
            longitude: dto.tgGeo.longitude,
            horizontalAccuracy: dto.tgGeo.horizontalAccuracy,
            observationId: observation.id,
          },
        });
      }

      let tgMediaGroup: TgMediaGroupItem[] = [];
      if (dto.tgMediaGroup) {
        tgMediaGroup = await Promise.all(
          dto.tgMediaGroup.map((item) =>
            tx.tgMediaGroupItem.create({
              data: {
                observationId: observation.id,
                tgAudioId: item.tgAudioId,
                tgDocumentId: item.tgDocumentId,
                tgPhotoId: item.tgPhotoId,
                tgVideoId: item.tgVideoId,
              },
              select: selectTgMediaGroupItem,
            })
          )
        );
      }

      return { ...observation, tgMediaGroup, tgGeo };
    });
  }

  async approveObservation(
    observationId: Observation["id"]
  ): Promise<Observation> {
    return this.prismaClient.observation.update({
      where: { id: observationId },
      data: { isApproved: true },
      select: selectObservation,
    });
  }

  async deleteObservation(observationId: Observation["id"]): Promise<void> {
    await this.prismaClient.observation.delete({
      where: { id: observationId },
    });
  }
}
