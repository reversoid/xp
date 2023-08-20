import {
  Body,
  Controller,
  Get,
  Param,
  Post,
  Put,
  Query,
  Request,
  UseGuards,
  ValidationPipe,
} from '@nestjs/common';
import { CreateObservationDTO } from './dto/create-observation.dto';
import { ObservationService } from './observation.service';
import { GetRandomObservations } from './dto/get-random-observations.dto';
import { AuthGuard } from '../auth/guards/auth.guard';
import { User } from '../user/entities/user.entity';
import { ApiOperation, ApiResponse, ApiTags } from '@nestjs/swagger';
import { ObservationResponse } from '../../shared/swagger/responses/ObservationResponse';
import { NumericIdParamDTO } from 'src/shared/dto/id.param.dto';
import { SeeManyObservationsDTO } from './dto/see-many-observations.dto';

@ApiTags('Observation')
@Controller('observation')
export class ObservationController {
  constructor(private observationService: ObservationService) {}

  @ApiOperation({ description: 'Create observation' })
  @ApiResponse({ description: 'New observation', type: ObservationResponse })
  @Post()
  @UseGuards(AuthGuard)
  async createObservation(
    @Request() { user }: { user: User },
    @Body() dto: CreateObservationDTO,
  ) {
    return this.observationService.createObservation(dto, user.id);
  }

  @ApiOperation({ description: 'Get random unseen observations' })
  @ApiResponse({
    description: 'Random unseen observations',
    type: ObservationResponse,
    isArray: true,
  })
  @Get('random')
  @UseGuards(AuthGuard)
  async getRandomObservations(
    @Request() { user }: { user: User },

    @Query(
      new ValidationPipe({
        transform: true,
        forbidNonWhitelisted: true,
      }),
    )
    { amount = 3 }: GetRandomObservations,
  ) {
    const observations = await this.observationService.getRandomObservations(
      amount,
      user.id,
    );
    return { observations };
  }

  @ApiOperation({ description: 'Mark observation as viewed' })
  @Put(':id/views')
  @UseGuards(AuthGuard)
  async markObservationAsViewed(
    @Request() { user }: { user: User },
    @Param() { id: observationId }: NumericIdParamDTO,
  ) {
    return this.observationService.markObservationAsViewed(
      user.id,
      observationId,
    );
  }

  @ApiOperation({ description: 'Mark many observations as viewed' })
  @Put('views')
  @UseGuards(AuthGuard)
  async markManyObservationsAsViewed(
    @Request() { user }: { user: User },
    @Body() { observations_ids }: SeeManyObservationsDTO,
  ) {
    return this.observationService.markManyObservationsAsViewed(
      user.id,
      observations_ids,
    );
  }
}
