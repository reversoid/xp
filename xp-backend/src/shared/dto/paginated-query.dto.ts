import { IsDateString, IsInt, IsOptional } from 'class-validator';
import { Type } from 'class-transformer';
import { DateTime } from 'luxon';

export class PaginationQueryDTO {
  @IsOptional()
  @IsInt()
  @Type(() => Number)
  limit?: number;

  @IsOptional()
  @IsDateString()
  @Type(() => DateTime.fromISO)
  lower_bound?: DateTime;
}
