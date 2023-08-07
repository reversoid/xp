import { Injectable, NotImplementedException } from '@nestjs/common';
import { CreateObservationDTO } from './dto/create-observation.dto';

@Injectable()
export class ObservationService {
  createObservation(dto: CreateObservationDTO, userId: number) {
    throw new NotImplementedException({ dto, userId });
  }

  /** Get given amount of random observations.
   *
   * *If userId is specified, it will ignore user with this id*
   */
  getRandomObservations(amount: number, userId?: number) {
    throw new NotImplementedException({ amount, userId });
  }
}
