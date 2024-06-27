import { PrismaClient } from "@prisma/client";
import { User } from "../../models/user.js";
import { CreateObservationDto } from "./types.js";
import { IdGenerator } from "../../utils/db/create-id.js";
import { Observation, selectObservation } from "../../models/observation.js";
import { TgGeo } from "../../models/tg-geo.js";
import {
  selectTgMediaGroupItem,
  TgMediaGroupItem,
} from "../../models/tg-media-group-item.js";

export class ObservationRepository {
  private readonly prismaClient: PrismaClient;

  private readonly idGenerator = new IdGenerator("observation");

  constructor({ prismaClient }: { prismaClient: PrismaClient }) {
    this.prismaClient = prismaClient;
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
        tgGeo = await tx.observationGeo.create({
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
            tx.observationMediaGroupItem.create({
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
}
