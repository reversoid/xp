import { IsDateString, IsOptional } from 'class-validator';
import { Type } from 'class-transformer';
import { DateTime } from 'luxon';
import { LimitQueryDTO } from './limit.query.dto';
import { ApiProperty } from '@nestjs/swagger';

export class PaginationQueryDTO extends LimitQueryDTO {
  @ApiProperty({
    type: 'string',
    format: 'date-time',
    required: false,
    description: 'Lower bound date',
  })
  @IsOptional()
  @IsDateString()
  @Type(() => DateTime.fromISO)
  lower_bound?: DateTime;
}
