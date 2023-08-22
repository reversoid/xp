import { ApiProperty } from '@nestjs/swagger';
import { ObservationResponse } from 'src/shared/swagger/responses/ObservationResponse';

export class RandomObservationResponse {
  @ApiProperty({ type: ObservationResponse, isArray: true })
  observations: ObservationResponse[];
}
