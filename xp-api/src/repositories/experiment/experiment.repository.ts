import { PrismaClient } from "@prisma/client";
import { IdGenerator } from "../../utils/db/create-id.js";
import {
  Experiment,
  experimentSchema,
  selectExperiment,
} from "../../models/experiment.js";
import { PaginatedData } from "../../utils/pagination/paginated-data.js";
import { User } from "../../models/user.js";
import { UpdateExperimentDto } from "./types.js";
import dayjs from "dayjs";
import { selectTgGeo, TgGeo } from "../../models/tg-geo.js";
import {
  selectTgMediaGroupItem,
  TgMediaGroupItem,
} from "../../models/tg-media-group-item.js";
import { decodeCursor, encodeCursor } from "../../utils/pagination/cursor.js";

export class ExperimentRepository {
  private readonly prismaClient: PrismaClient;
  private readonly idGenerator = new IdGenerator("experiment");

  constructor({ prismaClient }: { prismaClient: PrismaClient }) {
    this.prismaClient = prismaClient;
  }

  async getUserActiveExperiment(
    userId: User["id"]
  ): Promise<Experiment | null> {
    return this.prismaClient.experiment.findFirst({
      select: selectExperiment,
      where: {
        userId,
        canceledAt: null,
        completedAt: null,
        completeBy: { lte: new Date() },
      },
    });
  }

  async createEmptyExperiment(userId: User["id"]): Promise<Experiment> {
    return this.prismaClient.experiment.create({
      select: selectExperiment,
      data: {
        id: this.idGenerator.generateId(),
        completeBy: dayjs().add(24, "hours").toDate(),
        userId,
      },
    });
  }

  async fillExperiment(
    experimentId: Experiment["id"],
    dto: UpdateExperimentDto
  ): Promise<Experiment> {
    return this.prismaClient.$transaction(async (tx) => {
      const experiment = await tx.experiment.update({
        data: {
          tgDocumentId: dto.tgDocumentId,
          tgPhotoId: dto.tgPhotoId,
          tgText: dto.tgText,
          tgVideoId: dto.tgVideoId,
          tgVideoNoteId: dto.tgVideoNoteId,
          tgVoiceId: dto.tgVoiceId,
        },
        where: {
          id: experimentId,
          canceledAt: null,
          completedAt: null,
          completeBy: { lte: new Date() },
        },
        select: selectExperiment,
      });

      let tgGeo: TgGeo | null = null;
      if (dto.tgGeo) {
        tgGeo = await tx.tgGeo.create({
          data: {
            latitude: dto.tgGeo.latitude,
            longitude: dto.tgGeo.longitude,
            horizontalAccuracy: dto.tgGeo.horizontalAccuracy,
            experimentId: experiment.id,
          },
          select: selectTgGeo,
        });
      }

      let tgMediaGroup: TgMediaGroupItem[] = [];
      if (dto.tgMediaGroup) {
        tgMediaGroup = await Promise.all(
          dto.tgMediaGroup.map((item) =>
            tx.tgMediaGroupItem.create({
              data: {
                experimentId: experiment.id,
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

      return { ...experiment, tgGeo, tgMediaGroup };
    });
  }

  async getUserExperiments(
    userId: User["id"],
    options: { limit: number; creationOrder: "asc" | "desc"; cursor?: string }
  ): Promise<PaginatedData<Experiment>> {
    const decodedCursor = options.cursor ? decodeCursor(options.cursor) : null;

    const experiments = await this.prismaClient.experiment.findMany({
      where: { userId },
      take: options.limit + 1,
      orderBy: {
        privateId: options.creationOrder,
      },
      select: { ...selectExperiment, privateId: true },

      cursor: decodedCursor ? { privateId: decodedCursor } : undefined,
    });

    const cursor = experiments.at(options.limit)?.privateId;

    return {
      items: experiments
        .slice(0, options.limit)
        .map((e) => experimentSchema.parse(e)),
      cursor: cursor ? encodeCursor(cursor) : null,
    };
  }
}
