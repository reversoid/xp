import { ApiProperty } from '@nestjs/swagger';
import { ObservationResponse } from './ObservationResponse';
import {
  ISwaggerPaginatedResponse,
  SwaggerPaginatedResponse,
} from './Paginated.response';

export class ObservationPaginatedResponse
  extends SwaggerPaginatedResponse
  implements ISwaggerPaginatedResponse<ObservationResponse>
{
  @ApiProperty({ type: ObservationResponse, isArray: true })
  items: ObservationResponse[];
}
