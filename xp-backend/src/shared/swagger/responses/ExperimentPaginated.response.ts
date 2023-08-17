import { ApiProperty } from '@nestjs/swagger';
import {
  ISwaggerPaginatedResponse,
  SwaggerPaginatedResponse,
} from './Paginated.response';
import { ExperimentResponse } from './Experiment.response';

export class ExperimentPaginatedResponse
  extends SwaggerPaginatedResponse
  implements ISwaggerPaginatedResponse<ExperimentResponse>
{
  @ApiProperty({ type: ExperimentResponse, isArray: true })
  items: ExperimentResponse[];
}
