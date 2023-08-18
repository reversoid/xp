import { IsDateString, IsOptional } from 'class-validator';
import { Type } from 'class-transformer';
import { DateTime } from 'luxon';
import { LimitQueryDTO } from './limit.query.dto';

export class PaginationQueryDTO extends LimitQueryDTO {
  @IsOptional()
  @IsDateString()
  @Type(() => DateTime.fromISO)
  lower_bound?: DateTime;
}
