import { Observation } from "../../models/observation.js";
import { User } from "../../models/user.js";
import { ObservationRepository } from "../../repositories/observation/observation.repository.js";
import { CreateObservationDto } from "./types.js";

export class ObservationService {
  observationRepository: ObservationRepository;

  constructor({
    observationRepository,
  }: {
    observationRepository: ObservationRepository;
  }) {
    this.observationRepository = observationRepository;
  }

  async createObservation(
    userId: User["id"],
    dto: CreateObservationDto
  ): Promise<Observation> {
    return this.observationRepository.createObservation(userId, {
      tgDocumentId: dto.tgDocumentId,
      tgPhotoId: dto.tgPhotoId,
      tgText: dto.tgText,
      tgVideoId: dto.tgVideoId,
      tgVideoNoteId: dto.tgVideoNoteId,
      tgVoiceId: dto.tgVoiceId,
      tgMediaGroup: dto.tgMediaGroup,
      tgGeo: dto.tgGeo,
    });
  }
}